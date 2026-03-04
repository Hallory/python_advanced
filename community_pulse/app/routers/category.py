from flask import Blueprint, jsonify, request
from sqlalchemy import select
from pydantic import ValidationError

from app.schemas.category import CategoryResponse, CategoryCreateRequest
from app.models.category import Category
from app.extensions import db

categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories",
)

@categories_bp.route("", methods=["GET"])
def get_all_categories():
    stmt = select(Category)
    categories = db.session.execute(stmt).scalars().all()

    payload = [
        CategoryResponse.model_validate(obj).model_dump()
        for obj in categories
    ]
    return jsonify(payload), 200


@categories_bp.route("", methods=["POST"])
def create_category():
    raw_data = request.get_json(silent=True)
    if not raw_data:
        return jsonify({"error": "Request body is missing or not valid JSON"}), 400

    try:
        validated = CategoryCreateRequest.model_validate(raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    new_category = Category(**validated.model_dump())
    db.session.add(new_category)
    db.session.commit()

    payload = CategoryResponse.model_validate(new_category).model_dump()
    return jsonify(payload), 201


@categories_bp.route("/<int:category_id>", methods=["PUT"])
def update_one_category(category_id: int):
    raw_data = request.get_json(silent=True)
    if not raw_data:
        return jsonify({"error": "Request body is missing or not valid JSON"}), 400

    try:
        validated = CategoryCreateRequest.model_validate(raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if category is None:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    category.name = validated.name
    db.session.commit()

    payload = CategoryResponse.model_validate(category).model_dump()
    return jsonify(payload), 200


@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_one_category(category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    category = db.session.execute(stmt).scalars().one_or_none()

    if category is None:
        return jsonify({"error": f"Category with ID {category_id} not found"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": f"Category with ID {category_id} deleted successfully"}), 204
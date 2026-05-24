from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from dataset import prepare_data

def main():
    model_name = "distilbert-base-multilingual-cased"
    csv_path = "data/reviews.csv"
    
    print("Подготовка данных...")
    train_dataset, test_dataset, _ = prepare_data(csv_path, model_name)
    
    print("Загрузка модели...")
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        logging_dir='./logs',
        logging_steps=1,
        evaluation_strategy="epoch"
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
    )
    
    print("Запуск Fine-tuning...")
    trainer.train()
    
    model.save_pretrained("./fine_tuned_model")
    print("Модель успешно обучена и сохранена в './fine_tuned_model'!")

if __name__ == "__main__":
    main()
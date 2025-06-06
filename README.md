# Charaka AI - Medical Assistant

![Charaka AI Logo](BadmintonTableTennis/last.png)



![Show](BadmintonTableTennis/show.png)

## Features

- **Medical LLM**: Fine-tuned Huatuo-GPT model specifically for medical domain expertise
- **Multimodal Processing**: Analyzes patient video and audio for symptom detection
- **Efficient Fine-tuning**: Implemented QLoRA (Quantized Low-Rank Adaptation) for optimized model training
- **Diagnostic Assistance**: Offers evidence-based suggestions and medical information
- **Multilingual Support**: Handles consultations in multiple languages

![Dashboard Screenshot](BadmintonTableTennis/workflow-Photoroom.png)

## Technical Architecture

### Model

Charaka AI uses a fine-tuned version of Huatuo-GPT, a specialized medical language model. The model was further optimized using QLoRA to:
- Reduce memory requirements during fine-tuning
- Maintain high performance while improving efficiency
- Enable deployment on consumer-grade hardware

### Multimodal Pipeline

Video/Audio Input → Preprocessing → Feature Extraction → Medical LLM → Response Generation


## Contributing

Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Huatuo-GPT team for the base medical model
- QLoRA research team for quantization techniques
- Our medical advisors for domain expertise

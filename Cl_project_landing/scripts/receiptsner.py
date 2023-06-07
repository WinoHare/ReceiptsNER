import os
from google.api_core.client_options import ClientOptions
from google.cloud import documentai

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'scripts/google_auth_key.json'
settings = {
    "project_id": 'receiptsner',
    "location": 'eu',
    "processor_id": '10e6c537bbe8972c',
    "mime_type": 'image/jpeg'
}


def get_entities(file_path: str):
    opts = ClientOptions(api_endpoint=f"{settings['location']}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(settings['project_id'], settings['location'], settings['processor_id'])

    with open(file_path, "rb") as image:
        image_content = image.read()

    raw_document = documentai.RawDocument(content=image_content, mime_type=settings['mime_type'])
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    entities = {}
    receipt_date, total_amount, supplier_name, supplier_address = '', '', '', ''
    for item in document.entities:
        if item.type_ in ['receipt_date', 'total_amount', 'supplier_name']:
            entities[item.type_] = item.mention_text.replace('\n', '').strip()
        if item.type_ == 'receipt_date':
            receipt_date = item.mention_text
        if item.type_ == 'total_amount':
            total_amount = item.mention_text
        if item.type_ == 'supplier_name':
            supplier_name = item.mention_text
        if item.type_ == 'supplier_address':
            supplier_address = item.mention_text

    return receipt_date, total_amount, supplier_name, supplier_address



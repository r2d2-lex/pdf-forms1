from pdf_processing import ProcessPdf


data = {
    'Background': 'Русский1',
    'PlayerName': 'Русский22',
    'CharacterName': 'Русский333',
    'PersonalityTraits': 'Тест444',
}
# data = {
#     'Given Name Text Box': 'field111',
#     'Family Name Text Box': 'name222',
#     'Address 1 Text Box': 'nname333',
#     'City Text Box': '',
#     'Gender List Box': 'Panda',
#     'Height Formatted Field': '',
#     'Driving License Check Box': '/Off',
#     'Apt Number Text Box': '',
#     'Zipcode Text Box': '',
#     'Latin Check Box': '/Off',
#     'French Check Box': '',
#     'Esperanto Check Box': '',
#     'signature_1': '',
# }
TEMPLATE = 'form1.pdf'


def main():
    output_file = 'final_pdf.pdf'
    temp_files = []
    pdf = ProcessPdf('pdf_temp/', output_file)
    data_pdf = pdf.add_data_to_pdf(TEMPLATE, data)
    temp_files.append(data_pdf)
    # data_image_pdf = pdf.add_image_to_pdf(data_pdf, IMAGES, POSITIONS)
    # temp_files.append(data_image_pdf)
    # compressed_pdf = pdf.compress_pdf(data_image_pdf)

    # pdf.delete_temp_files(temp_files)


if __name__ == '__main__':
    main()
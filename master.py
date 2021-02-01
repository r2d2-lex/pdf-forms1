import sys
from pdf_processing import ProcessPdf


data = {
    'Background': 'РуссКий1',
    'PlayerName': 'РуССкий22',
    'CharacterName': 'РусскиЙ333',
    'PersonalityTraits ': 'Давно выяснено,\n текст ,\r ещё немного текста \r\n + Ещё чуть чуть',
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
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            usage()
            sys.exit()

        output_file = 'final_pdf.pdf'
        temp_files = []
        pdf = ProcessPdf('pdf_temp/', output_file)
        data_pdf = pdf.add_data_to_pdf(sys.argv[1], data)
        temp_files.append(data_pdf)
        # data_image_pdf = pdf.add_image_to_pdf(data_pdf, IMAGES, POSITIONS)
        # temp_files.append(data_image_pdf)
        # compressed_pdf = pdf.compress_pdf(data_image_pdf)

        # pdf.delete_temp_files(temp_files)
    else:
        usage()
    print('exit...')


def usage():
    print("usage: {0} template.pdf".format(sys.argv[0]))


if __name__ == '__main__':
    main()
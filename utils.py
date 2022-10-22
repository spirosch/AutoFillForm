
import yaml

def test():
    path = "G:\Running Projects\AutoFillForm\\first_form_template_f.yml"
    with open(path,encoding='utf-8') as form_yaml:
        form_data = yaml.load(form_yaml, Loader=yaml.FullLoader)
    return form_data



def file_to_py():
    pass


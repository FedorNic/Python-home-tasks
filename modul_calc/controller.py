import model_sub as model, ui

def button():
    value_a = ui.get_value()
    value_b = ui.get_value()
    model.init(value_a, value_b)
    result = model.log()
    ui.view(result)
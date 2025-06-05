from ._anvil_designer import Form1Template
from anvil import *
import anvil


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_hide(self, **event_args):
    """This method is called when the form is removed from the page"""
    pass

  def categorise_button_click_click(self, **event_args):
    """This method is called when the button is clicked"""
    nume = self.nume.text
    
    prenume = self.prenume.text
    
    varsta = self.varsta.text

    judet = self.judet.text

    patients = anvil.server.call('predict_cancer', 
                                 nume, 
                                 prenume, 
                                 varsta, 
                                 judet)
    if patients:
      self.type_of_cancer_label.visible = True
      self.type_of_cancer_label.text = 'Pacientul sufera de cancer numit' + patients.capitalize()

  def varsta_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
      
    
    


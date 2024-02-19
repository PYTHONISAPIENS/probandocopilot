import UIKit

class FormViewController: UIViewController {
    @IBOutlet weak var datePicker: UIDatePicker!
    @IBOutlet weak var sysPressureTextField: UITextField!
    @IBOutlet weak var diaPressureTextField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Configurar el formato de fecha y hora del date picker
        datePicker.datePickerMode = .dateAndTime
        
        // Configurar el teclado numérico para los campos de presión
        sysPressureTextField.keyboardType = .numberPad
        diaPressureTextField.keyboardType = .numberPad
    }
    
    @IBAction func submitButtonTapped(_ sender: UIButton) {
        // Obtener los valores ingresados por el usuario
        let selectedDate = datePicker.date
        let sysPressure = sysPressureTextField.text ?? ""
        let diaPressure = diaPressureTextField.text ?? ""
        
        // Realizar las operaciones necesarias con los datos capturados
        
        // Ejemplo: Imprimir los valores en la consola
        print("Fecha y hora seleccionadas: \(selectedDate)")
        print("Presión sistólica: \(sysPressure)")
        print("Presión diastólica: \(diaPressure)")
        
        // Aquí puedes agregar la lógica adicional que necesites
        
        // Limpiar los campos después de enviar el formulario
        sysPressureTextField.text = ""
        diaPressureTextField.text = ""
    }
}


### Learn complete HashMap in Pyhton  Here 
'''
General case represents that developer working on 
frontend cannot work backend development unless he/she is fullstack dev.
Write a method named verifier () that checks this condition.
The method should check that if frontend is True and backend is True,
the method returns Fullstack as string. If one of them is True, it should return
the respective desgination, and if none of them are true, it returns,
not a developer respetively.
'''
class Employee:
    def __init__(self, designation: str = 'Developer', frontend: bool = False, backend: bool = False):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__(self):
        return f'Designation: {self.designation}, Frontend: {self.frontend}, Backend: {self.backend}'
    
    def verifier(self):
        if self.frontend and self.backend:
            return "Fullstack"
        elif self.frontend:
            return "Frontend Developer"
        elif self.backend:
            return "Backend Developer"
        else:
            return "Not a Developer"

if __name__ == '__main__':
    abc = input("Enter the Designation: ")
    
    frontend_input = input("Is this employee working on frontend? (yes/no): ").strip().lower()
    backend_input = input("Is this employee working on backend? (yes/no): ").strip().lower()

    frontend = frontend_input == "yes"
    backend = backend_input == "yes"

    employee = Employee(abc, frontend, backend)
    print(employee)
    print("Role:", employee.verifier())

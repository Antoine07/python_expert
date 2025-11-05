
class ClassRoom:
    def __init__(self, name, students):
        self.name = name
        self.students = students # ATTRIBUTS
        
    def addStudent(self, student):
        self.students.append(student)
        
class Student:
    def __init__(self, name):
        self.name = name

socrates = Student("Socrates")
sylvain = Student("Sylvain")
olivia = Student("Olivia")
rayan = Student("Rayan")

students = [socrates, sylvain, olivia, rayan]

print(socrates.name)

estiam_paris_lyon_e2 = ClassRoom("ESTIAM_PARIS_LYON_E2", students)

petinia = Student("Petinia")
estiam_paris_lyon_e2.addStudent(petinia)

# Afficher la liste des étudiants avec leurs noms
print(estiam_paris_lyon_e2.students)

for i in range(len(estiam_paris_lyon_e2.students)):
    print(estiam_paris_lyon_e2.students[i].name)
    
# on récupère l'ensemble des students dans la liste ce sont des objets Student
for student in estiam_paris_lyon_e2.students:
    print(student.name) # affiche leur nom (attribut name dans la classe Student)
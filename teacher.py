class teacher:
    def readsub(self):
        print("teacher advises to read")
class lazystudent(teacher):
    def readsub(self):
        print("no study no job")
class perfect(teacher):
    def readsub(self):
        print("study and practise")
p=perfect()
p.readsub()
l=lazystudent()
l.readsub()

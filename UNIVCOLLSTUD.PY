import cx_Oracle
class university:
    def univdet(self):
        self.uname=input("enter university Name:")
        self.uloc=input("enter univ location:")
    def dispuniv(self):
        print("university name:",self.uname)
        print("university location:",self.uloc)

class college(university):
    def colldet(self):
        cname=input("enter college name:")
        cloc=input("enter college details:")
    def dispcoll(self):
        print("college name:",self.cname)
        print("college loc:",self.cloc)
class student(college):
    def studdet(self):
        self.sname=input("enter student name:")
        self.sno=input("enter sno:")
        self.crs=input("enter student crs:")
    def dispstud(self):
        print("student name:",self.sname)
        print("student no:",self.sno)
        print("student crs:",self.crs)
    def savedata(self):
        con=cx_Oracle.connect("system/Nandu123@localhost,XE")
        cur=con.cursor()
        cur.execute("insert into university values('%s','%s','%s','%s',%d,'%s''%s')"
                    %(self.uname,self.uloc,self.cname,self.cloc,self.sno,self.sname,self.crscrs))
        con.commit()
        print("university details")
        print("university name:",self.uname)
        print("university loc:",self.uloc)
        print("_"*40)
        print("college details")
        print("college namre:",self.cname)
        print("college location",self.cloc)
        print("_"*30)
        print("student details")
        print("student no",self.sno)
        print("student name:",self.sname)
        print("stu crs:",)
s=student()
s.univdet()
s.dispuniv()
s.colldet()
s.dispcoll()
s.studdet()
s.dispstud()
s.savedata()




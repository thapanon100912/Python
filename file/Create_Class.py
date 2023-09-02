# การสร้าง Class
class Employee :
    __data = {"name":None,"salary" : None,"office":None}
    # ระบบ
    def __testforit(namein = 'str',salaryin = 1,officein = 'str') :
        if type(namein) != str : raise TypeError('The variable "name" cannot be specified other than str.')
        if type(salaryin) != int : raise TypeError('The variable "salary" cannot be specified other than int.')
        if type(officein) != str : raise TypeError('The variable "office" cannot be specified other than str.')

        return True

    def __init__(self,name,salary,office = None) -> None :
            Employee.__testforit(name,salary,office)
            name = str(name)
            salary = int(salary)
            office = str(office)
            self.__data["name"] = name
            self.__data["salary"] = salary
            self.__data["office"] = office
            
    # help
    def help() -> str :
        print('สวัสดีนี่คือวิธีใช้ :\n1. เราต้องสร้าง object ก่อน list *โดย* ข้างบนข้ามแก้ไข ให้แก้ตรงที่สร้างวัตถุที่กำหนดไว้ให้\n2. คำสั่งสร้าง Object : <ชื่อ Object> = Employee(<ชื่อ>,<เงินเดือน>)\tตัวอย่าง : employeee001 = Employee\n')
        print('คำสั่งทั่วไป : (ชื่อ Object จะถูกแทนด้วย obj)\n- Employee.help() = ช่วยเหลือ\n- obj.show_detail() = แสดงข้อมูลของ obj นั้นๆ\n- obj.getname() = ส่งกลับข้อมูลชื่อ\n- obj.getsalary() = ส่งกลับข้อมูลเงินเดือน\n')
        print('คำสั่งขั้นสูง : (ชื่อ Object จะถูกแทนด้วย obj)\n- obj._setname(<ชื่อใหม่>) = ตั้งชื่อใหม่\n- obj._setsalary(<เงินเดือนใหม่>) = ตั้งเงินเดือนใหม่\n')
        print('คำสั่งข้อมูลขั้นสูง : (ชื่อ Object จะถูกแทนด้วย obj')
    # ดูข้อมูล
    def show_detail(self) -> None : print('ชื่อ : {}\nเงินเดือน : {}\nตำแหน่ง : {}'.format(self.__data["name"] , self.__data["salary"] , self.__data["office"]))
    # get ข้อมูล
    def getname(self) -> str : return self.__data["name"]
    def getsalary(self) -> int : return self.__data["salary"]
    def getoffice(self) -> str : return self.__data["office"]
    def __str__(self) -> str: return self.__data["name"]
    # ตั้งชื่อ/เงินเดือน/ตำแหน่ง
    def _setname(self,newname:str) -> None :
        Employee.__testforit(newname)
        newname = str(newname)
        self.__data["name"] = newname
    def _setsalary(self,newsalary:int) -> None :
        Employee.__testforit(salaryin=newsalary)
        newsalary = int(newsalary)
        self.__data["salary"] = newsalary
    def _setoffice(self,newoffice = 'None') -> None :
        Employee.__testforit(officein=newoffice)
        newoffice = str(newoffice)
        self.__data["office"] = newoffice

# การสร้างวัตถุ
Employee.help()
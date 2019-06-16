import time as t1


class empappriasal:
    currentsalary=0.0
    noofyears=0
    empname=""
    perfindex=0
    persindex=0
    
    
    def calappraisal(self):
        f=open("AppraisalFile.txt","a")
        if self.noofyears <= 2:
            appr=eval("(self.persindex/10*1000)+(self.perfindex/10*1000)+(self.currentsalary*.1)+self.currentsalary")
            print("The new Salary after appraisal for %s is %f"%(self.empname,appr))
            f.write("********************************************* \n")
            f.write("The new Salary after appraisal for %s is %f \n"%(self.empname,appr))
            f.write("********************************************* \n")
            
        elif self.noofyears <= 3:
            appr=eval("(self.persindex/10*1000)+(self.perfindex/10*1000)+(self.currentsalary*.2)+self.currentsalary")
            print("The new Salary after appraisal for %s is %f"%(self.empname,appr))
            f.write("********************************************* \n")
            f.write("The new Salary after appraisal for %s is %f \n"%(self.empname,appr))
            f.write("********************************************* \n")
            
        elif self.noofyears > 3:
            appr=eval("(self.persindex/10*1000)+(self.perfindex/10*1000)+(self.currentsalary*.3)+self.currentsalary")
            print("The new Salary after appraisal for %s is %f"%(self.empname,appr))
            f.write("********************************************* \n")
            f.write("The new Salary after appraisal for %s is %f \n"%(self.empname,appr))
            f.write("********************************************* \n")
        f.close()

print("*** Welcome to Employee Appriasal Calculation System ***")
username = input("Enter the username: ")



if username=="Mayank":
    password = input("Enter the password: ")
    if password=="abcd":
        f1=open("AppraisalLogs.txt","a")
        tstr=t1.strftime("%c")
        str(tstr)
        f1.write("***************** \n")
        f1.write("Login Time is %s \n"%tstr)
        f1.write("Username: %s \n"%username)
        f1.write("***************** \n")
        f1.close()
        emp1=empappriasal()
        emp1.empname=input("Enter the Employee Name : ")
        emp1.currentsalary=float(input("Enter your current Salary: "))
        emp1.noofyears=int(input("Enter Number of years served by employee: "))
        emp1.perfindex=int(input("Enter the Performance index of Last year(1-10) : "))
        emp1.persindex=int(input("Enter the Personal index of last year(1-10) : "))
        
        emp1.calappraisal()
    else:
        print("Bad password")
        f1=open("AppraisalLogs.txt","a")
        tstr=t1.strftime("%c")
        str(tstr)
        f1.write("***************** \n")
        f1.write("Login Time is %s \n"%tstr)
        f1.write("Username: %s tried a BAD LOGIN \n"%username)
        f1.write("***************** \n")
        f1.close()
elif username=="Anil":
    password = input("Enter the password: ")
    if password=="efgh":
        f1=open("AppraisalLogs.txt","a")
        tstr=t1.strftime("%c")
        str(tstr)
        f1.write("***************** \n")
        f1.write("Login Time is %s \n"%tstr)
        f1.write("Username: %s \n"%username)
        f1.write("***************** \n")
        f1.close()
        emp1=empappriasal()
        emp1.empname=input("Enter the Employee Name: ")
        emp1.currentsalary=float(input("Enter your current Salary"))
        emp1.noofyears=int(input("Enter Number of years served by employee"))
        emp1.perfindex=int(input("Enter the Performance index of Last year(1-10) : "))
        emp1.persindex=int(input("Enter the Personal index of last year(1-10) : "))
        
        emp1.calappraisal()
    else:
        print("Bad Password")
        f1=open("AppraisalLogs.txt","a")
        tstr=t1.strftime("%c")
        str(tstr)
        f1.write("***************** \n")
        f1.write("Login Time is %s \n"%tstr)
        f1.write("Username: %s tried a BAD LOGIN \n"%username)
        f1.write("***************** \n")
        f1.close()
else:
    print("Bad Username")
    f1=open("AppraisalLogs.txt","a")
    tstr=t1.strftime("%c")
    str(tstr)
    f1.write("***************** \n")
    f1.write("Login Time is %s \n"%tstr)
    f1.write("Username: %s tried a BAD LOGIN \n"%username)
    f1.write("***************** \n")
    f1.close()

    

        
    
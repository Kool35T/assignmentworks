using System;
using System.Collections.Generic;

namespace HRMaster
{
    public class Employee
    {
        public string NRIC { get; set; }
        public string Name { get; set; }
        public string Salutation { get; set; }
        public DateTime Date { get; set; }
        public string Designation { get; set; }
        public string Department { get; set; }
        public string MobileNo { get; set; }
        public string HireType { get; set; }
        public double Salary { get; set; }
        public double MonthlyPayout { get; set; } = 0.0;
        public Employee(string NRIC, string Name, string Salutation, DateTime Date, string Designation, string Department, string MobileNo, string HireType, double Salary)
        {
            this.NRIC = NRIC;
            this.Name = Name;
            this.Salutation = Salutation;
            this.Date = Date;
            this.Designation = Designation;
            this.Department = Department;
            this.MobileNo = MobileNo;
            this.HireType = HireType;
            this.Salary = Salary;
        }
        public string generateCorpAdmin()
        {
            return $"{this.Name}, {this.Designation}, {this.Department}";
        }
        public string generateInfoForITDepartment()
        {
            return $"{this.Salutation}, {this.Name}, {this.MobileNo}, {this.Designation}, {this.Department}";
        }
        public string generateInfoForProcurement()
        {
            return $"{this.NRIC}, {this.Name}, {this.Department}, {this.MobileNo}";
        }
    }
}
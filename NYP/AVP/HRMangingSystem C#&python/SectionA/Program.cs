using System;
using System.IO;
using System.Collections.Generic;

namespace HRMaster
{
    public class Program
    {
        public static void generateInfoForCorpAdmin(List<Employee> employees)
        {
            try
            {
                string path = "../CorporateAdmin.txt";
                using (StreamWriter sw = new StreamWriter(path))
                {
                    foreach (Employee e in employees)
                    {
                        string line = e.generateCorpAdmin();
                        sw.WriteLine(line);
                    }
                }
            }
            catch (IOException e)
            {
                Console.WriteLine(e);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        public static void generateInfoForProcurement(List<Employee> employees)
        {
            try
            {
                string path = "../Procurement.txt";
                using (StreamWriter sw = new StreamWriter(path))
                {
                    foreach (Employee e in employees)
                    {
                        string line = e.generateInfoForProcurement();
                        sw.WriteLine(line);
                    }
                }
            }
            catch (IOException e)
            {
                Console.WriteLine(e);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        public static void generateInfoForITDepartment(List<Employee> employees)
        {
            try
            {
                string path = "../ITDepartment.txt";

                using (StreamWriter sw = new StreamWriter(path))
                {
                    foreach (Employee e in employees)
                    {
                        string line = e.generateInfoForITDepartment();
                        sw.WriteLine(line);
                    }
                }
            }
            catch (IOException e)
            {
                Console.WriteLine(e);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        public static List<Employee> readHRMasterList()
        {
            string path = @"../HRMasterList.txt";
            List<Employee> employees = new List<Employee>();
            if (File.Exists(path)) // prevent an I/O error
            {
                using (StreamReader sr = File.OpenText(path))
                {
                    string s;
                    while ((s = sr.ReadLine()) != null)
                    {
                        string[] employeeData = s.Split('|');
                        Employee e = new Employee(
                            NRIC: employeeData[0],
                            Name: employeeData[1],
                            Salutation: employeeData[2],
                            Date: Convert.ToDateTime(employeeData[3]),
                            Designation: employeeData[4],
                            Department: employeeData[5],
                            MobileNo: employeeData[6],
                            HireType: employeeData[7],
                            Salary: Convert.ToDouble(employeeData[8])
                        );
                        employees.Add(e);
                    }
                }
            }
            else
            {
                Console.WriteLine("Error: File cannot be found");
            }
            return employees;
        }

        public delegate void del(List<Employee> employees);

        public static void Main()
        {
            List<Employee> employees = readHRMasterList();
            del del1 = generateInfoForITDepartment;
            del del2 = generateInfoForCorpAdmin;
            del del3 = generateInfoForProcurement;
            del del4 = del1 + del2 + del3;
            del4(employees);

        }
    }
}
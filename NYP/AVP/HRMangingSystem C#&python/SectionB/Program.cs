using HRMaster;

namespace SectionB
{
    public enum HireType
    {
        PartTime = 50,
        FullTime = 100,
        Hourly = 25
    }
    public class Program
    {
        public static void Main()
        {
            try
            {
                List<Employee> employees = HRMaster.Program.readHRMasterList();
                Asyncforpayroll(employees);
                updateMonthlyPayoutToMasterlist(employees);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        public static Task<List<Employee>> Asyncforpayroll(List<Employee> employees)
        {
            Task<List<Employee>> TaskforprocessPayroll = Task.Run(() => processPayroll(employees));
            return TaskforprocessPayroll;
        }

        public static List<Employee> processPayroll(List<Employee> employees)
        {
            foreach (Employee e in employees)
            {
                e.MonthlyPayout = e.Salary / 100 * (double)Enum.Parse<HireType>(e.HireType);
            }
            foreach (Employee e in employees)
            {
                Console.WriteLine($"{e.Name} ({e.NRIC})");
                Console.WriteLine($"{e.Designation}");
                Console.WriteLine($"{e.HireType} Payout: ${e.MonthlyPayout}");
                Console.WriteLine("------------------------------------");
            }
            double totalmonthlypayout = 0;
            foreach (Employee e in employees)
            {
                totalmonthlypayout += e.MonthlyPayout;
            }
            Console.WriteLine($"Total Monthly Payout: {totalmonthlypayout}");
            return employees;
        }
        public static void updateMonthlyPayoutToMasterlist(List<Employee> employees)
        {
            try
            {
                string path = "../HRMasterlistB.txt";
                using (StreamWriter sw = new StreamWriter(path))
                {
                    foreach (Employee e in employees)
                    {
                        DateTime n = e.Date;
                        string date = n.ToString("dd/MM/yyyy");
                        string line = $"{e.NRIC}|{e.Name}|{e.Salutation}|{date}|{e.Designation}|{e.Department}|{e.MobileNo}|{e.HireType}|{e.Salary}|{e.MonthlyPayout}";
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
    }
}

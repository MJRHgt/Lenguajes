using System;
using System.Xml;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.IO;


namespace ConsoleApp4
{
    internal class Program
    {

        static void Main(string[] args)
        {
            string cadena = "";
            Console.WriteLine("ingrese ruta de archivo de configuracion");
            cadena =Console.ReadLine();
            string cadenae = "";
            Console.WriteLine("ingrese cadena a evaluar");
            cadenae = Console.ReadLine();
            string path = Path.GetFullPath(@"C:PDA.py");
            Console.WriteLine(path);
            path = path;
            ScriptRuntime py = Python.CreateRuntime();
            dynamic pyProgram = py.UseFile(path);

            pyProgram.main(cadena,cadenae);

            Console.ReadKey();
        }


    }
}



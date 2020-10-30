class cliente {
    rut;
    nombre;
    apellido;
    fechaNacimiento;

    setRut(rut) { this.rut = rut; }
    setNombre(nombre) { this.nombre = nombre; }
    setApellido(apellido) { this.apellido = apellido; }
   
    getRut() { return this.rut; }
    getNombre() { return this.nombre; }
    getApellido() { return this.apellido; }
  


    imprimir() {
        return "Rut:" + this.rut + " Nombre:" +
            this.nombre + " Apellido:" + this.apellido  ;
    }
}
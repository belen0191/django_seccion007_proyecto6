class producto {
    marca;
    producto;
    precio;
    descripcion;

    setMarca(marca) { this.marca = marca; }
    setProducto(producto) { this.producto = producto; }
    setPrecio(precio) { this.precio = precio; }
    setDescripcion(descripcion) { this.descripcion = descripcion; }
   
    getMarca() { return this.marca; }
    getProducto() { return this.producto; }
    getPrecio() { return this.precio; }
    getDescripcion() { return this.descripcion; }
  


    imprimir() {
        return "Marca:" + this.marca + "Producto:" + this.producto + " Precio:" +
            this.precio + " Descripcion:" + this.descripcion  ;
    }
}
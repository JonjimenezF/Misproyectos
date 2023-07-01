
//Contenedor producto
function listarProducto(idProducto){
    var producto = document.getElementById(idProducto);
    var nombre = producto.querySelector('h5').textContent;
    var imagen = producto.querySelector('img');
    var imagensrc = imagen.src;
    var precio = producto.querySelector('input').value;
    var precioString = producto.querySelector('h3').textContent;
    const productoArray = {
        titulo: nombre,
        img: imagensrc,
        precio: precio,
        precioString: precioString
    }
    return productoArray;
}


function agregarCarrito(idProducto){//Llamamos a la id producto(produco_1,etc)

   var producto = listarProducto(idProducto);
   var tbody = document.getElementById('productos-carrito'); 
   var fila = document.createElement('tr');//creamos fila <tr> </tr>
   
   var celdaImg=document.createElement('td');//creamos la columna de la fila(td)
   imagen=document.createElement('img');//creamos una etiqueta <img >
   imagen.src=producto.img;//<img src="#">
   imagen.classList.add('img-carrito');//<img src="" class="img-carrito">
   celdaImg.appendChild(imagen);//<td> <img src="" class="img-carrito"> </td>

   var celdaTitulo=document.createElement('td');//<td> </td>
   celdaTitulo.textContent=producto.titulo;//<td>producto.titulo</td>
   
   var celdaPrecio=document.createElement('td');//<td> </td>
   celdaPrecio.textContent=producto.precioString;//<td>producto.precioString</td>
   
   var precioNormal=document.createElement('input');//<input>
   precioNormal.setAttribute('value',producto.precio); //<input value="producto.precio">
   precioNormal.style.display="none";//<input value="producto.precio" style="display:none;">
   precioNormal.classList.add('precio-producto');//<input value="producto.precio" style="display:none;" class="precio-producto">
   celdaPrecio.append(precioNormal);

   
   fila.appendChild(celdaImg);  /*  <tr> 
                                        <td> <img src="" class="img-carrito"> </td>
                                    </tr>
                                */
   fila.appendChild(celdaTitulo);/* <tr> 
                                        <td> <img src="" class="img-carrito"> </td>
                                        <td>producto.titulo</td> 
                                    </tr>
                                 */
   fila.appendChild(celdaPrecio);/* <tr> 
                                        <td> <img src="" class="img-carrito"> </td>
                                        <td>producto.titulo</td> 
                                        <td>producto.precioString</td>
                                    </tr>
                                    */

   tbody.appendChild(fila);/* <tbody id="productos-carrito">
                                    <tr> 
                                        <td> <img src="" class="img-carrito"> </td>
                                        <td>producto.titulo</td> 
                                        <td>producto.precioString</td>
                                    </tr>                                               
                              </tbody>
   
   
   */

   var celdaPrecioFinal = document.getElementById('precioFinal');
   var precios= document.getElementsByClassName('precio-producto');
   var total = 0;
   for (var i=0; i<precios.length; i++){
        var precioActual=parseFloat(precios[i].value);
        if(!isNaN(precioActual)){
            total+=precioActual
        }
   }
   var totalFormateado = formatearPrecio(total);
   celdaPrecioFinal.textContent='Total: ' + totalFormateado;//<b class="m-4" id="precioFinal">'Total: ' + totalFormateado</b>
}

function formatearPrecio(precio) {
    // Convertir el precio a string
    var precioString = precio.toString();
  
    // Separar la parte entera en grupos de tres dígitos
    var grupos = [];
    while (precioString.length > 3) {
      grupos.unshift(precioString.slice(-3));
      precioString = precioString.slice(0, -3);
    }
    grupos.unshift(precioString);
  
    // Unir los grupos con puntos
    var precioFormateado = '$' + grupos.join('.');
  
    return precioFormateado;
  }

function limpiarCarrito() {
    var carrito = document.getElementById('productos-carrito');
  
    // Eliminar todos los hijos del carrito
    while (carrito.firstChild) {
      carrito.removeChild(carrito.firstChild);
    }
    var celdaPrecioFinal = document.getElementById('precioFinal');
    celdaPrecioFinal.textContent='';
  }

  
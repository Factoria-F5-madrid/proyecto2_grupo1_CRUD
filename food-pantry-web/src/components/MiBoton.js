// src/components/MiBoton.js

import React from 'react'; // Necesario para usar JSX

// Un componente funcional es una función de JavaScript
function MiBoton(props) {
  // `props` son las propiedades que se le pasan al componente
  // En este caso, esperamos una propiedad 'texto' y una 'onClick'

  const handleClick = () => {
    if (props.onClick) {
      props.onClick(); // Llama a la función pasada por la prop onClick
    }
    alert(`¡Hiciste clic en el botón: ${props.texto}!`);
  };

  return (
    <button
      onClick={handleClick}
      style={{
        padding: '10px 20px',
        fontSize: '16px',
        backgroundColor: '#007bff',
        color: 'white',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
        margin: '5px'
      }}
    >
      {props.texto || 'Haz clic'} {/* Muestra el texto de la prop o un valor por defecto */}
    </button>
  );
}

// Exporta el componente para poder usarlo en otros archivos
export default MiBoton;
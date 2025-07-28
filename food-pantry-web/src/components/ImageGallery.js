import React, { useState, useEffect } from 'react';

// Importa tus imágenes de la galería aquí
// Asegúrate de que las rutas sean correctas
// Puedes añadir más si quieres
import img1 from '../assets/volunteer1.jpg';
import img2 from '../assets/alimentos1.jpg';
import img3 from '../assets/servicio1.jpg';
import img4 from '../assets/arreglo.jpg';
import img5 from '../assets/entrega1.jpg';


const images = [img1, img2, img3, img4, img5]; // Array de tus imágenes importadas

function ImageGallery() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const intervalTime = 5000; // 5 segundos

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, intervalTime);

    // Limpieza del intervalo cuando el componente se desmonta
    return () => clearInterval(timer);
  }, []); // El array vacío asegura que el efecto se ejecute solo una vez al montar

  return (
    <div style={{
      width: '80%',
      margin: '40px auto', // Margen superior e inferior para separarlo del contenido
      overflow: 'hidden',
      position: 'relative',
      borderRadius: '8px',
      boxShadow: '0 4px 10px rgba(0,0,0,0.3)',
      height: '400px', // Altura fija para la galería
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: '#eee' // Color de fondo si no hay imagen
    }}>
      {images.map((image, index) => (
        <img
          key={index}
          src={image}
          alt={`Galería imagen ${index + 1}`}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover', // Cubre el área manteniendo la relación de aspecto
            position: 'absolute',
            opacity: index === currentIndex ? 1 : 0,
            transition: 'opacity 1s ease-in-out', // Transición suave entre imágenes
          }}
        />
      ))}
    </div>
  );
}

export default ImageGallery;
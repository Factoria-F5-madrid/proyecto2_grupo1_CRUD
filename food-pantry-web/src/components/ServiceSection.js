
import React from 'react';
import distribucionImg from '../assets/reparto2.jpg';
import voluntariadoImg from '../assets/volunteer1.jpg';
import donacionesImg from '../assets/arreglo.jpg';
// More services


const services = [
  {
    name: 'Distribución de Alimentos',
    image: distribucionImg,
    description: 'Entregamos alimentos a quienes más lo necesitan a través de nuestra red de organizaciones colaboradoras.',
  },
  {
    name: 'Voluntariado',
    image: voluntariadoImg,
    description: 'Nuestros voluntarios son el corazón de nuestra misión, ayudando en todas las etapas del proceso.',
  },
  {
    name: 'Recolección de Donaciones',
    image: donacionesImg,
    description: 'Organizamos campañas para recoger alimentos y recursos de la comunidad y empresas.',
  },
  // Añade más servicios aquí si lo deseas
];
const ComponenteUno = () => {
  return (
    
    <div className="flex flex-col items-center justify-center min-h-screen p-8 bg-gray-50">
      <ComponenteUno />
      {/* Línea decorativa con degradado */}
 
    </div>
  );
};


function ServiceSection() {
  return (
     <section style={{ margin: '60px auto', width: '80%', textAlign: 'center' }}>
      {/* <div className="w-full h-1 my-12 bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 rounded-full"></div> */}
      <h2 style={{ fontSize: '2.5em', marginBottom: '40px', color: '#333' }}>Nuestros Servicios</h2>
      <div style={{
        display: 'flex',
        flexWrap: 'wrap', // Permite que los elementos se envuelvan a la siguiente línea
        justifyContent: 'center', // Centra los elementos horizontalmente
        gap: '30px', // Espacio entre los elementos
      }}>
        {services.map((service, index) => (
          <div
            key={index}
            style={{
              flexBasis: '280px', // Ancho base para cada tarjeta de servicio
              flexGrow: 1, // Permite que las tarjetas crezcan para llenar el espacio
              backgroundColor: '#f9f9f9',
              padding: '20px',
              borderRadius: '10px',
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              textAlign: 'center',
            }}
          >
            <img
              src={service.image}
              alt={service.name}
              style={{
                width: '180px', // Tamaño fijo para la imagen
                height: '180px',
                borderRadius: '50%', // Para hacerla circular
                objectFit: 'cover',
                marginBottom: '15px',
                border: '4px solid #4CAF50', // Borde para resaltar la imagen
              }}
            />
            <h3 style={{ fontSize: '1.5em', marginBottom: '10px', color: '#555' }}>{service.name}</h3>
            <p style={{ fontSize: '1em', color: '#777' }}>{service.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default ServiceSection;
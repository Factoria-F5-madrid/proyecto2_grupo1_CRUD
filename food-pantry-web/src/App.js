// App.js
import React from 'react';
import './App.css';

import ImageGallery from './components/ImageGallery';
import ServiceSection from './components/ServiceSection'; // Importa el componente de servicios
import Footer from './components/Footer'; // Importa el componente de pie de página

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <ul style={{ listStyle: 'none', padding: 0, display: 'flex', justifyContent: 'center' }}>
            <li style={{ margin: '0 15px' }}>
              <a href="/quienes-somos" style={{ color: 'white', textDecoration: 'none' }}>Quiénes Somos</a>
            </li>
            <li style={{ margin: '0 15px' }}>
              <a href="/donativos" style={{ color: 'white', textDecoration: 'none' }}>Donativos</a>
            </li>
            <li style={{ margin: '0 15px' }}>
              <a href="/contacto" style={{ color: 'white', textDecoration: 'none' }}>Contacto</a>
            </li>
          </ul>
        </nav>
        <h1>EatTogether</h1>
      </header>

      <main>
      <section style={{ margin: '20px 0' }}>
  <img
    src={require('./assets/volunteer1.jpg')}
    alt="Imagen representativa de un banco de alimentos"
    style={{
      maxWidth: '80%', // Limita el ancho al 80% del contenedor padre
      maxHeight: '600px', // Por ejemplo, un máximo de 400 píxeles de alto
      width: 'auto', // Asegura que el ancho se ajuste automáticamente
      height: 'auto', // Asegura que la altura se ajuste automáticamente
      objectFit: 'contain', // O 'cover', dependiendo de lo que quieras
      borderRadius: '80px',
      boxShadow: '0 4px 8px rgba(0,0,0,0.2)'
    }}
  />
</section>
    <div className='texto1'>
      <p> Alimentos para Todos: Tu Banco en Madrid.<br />
      EatTogether, transforma excedentes en esperanza.<br /> Juntos, garantizamos que nadie pase hambre en Madrid.<br /> Donar alimentos, ayudar y combatir la necesidad es nuestra misión.<br /></p>
    </div>

    

        <section>
        <ImageGallery />
        </section>

        {/* Nueva sección para los servicios */
        }

<div className="cute-gradient-divider"></div>
  <ServiceSection />

        <p style={{ marginTop: '40px' }}>Bienvenido a la página principal del Banco de Alimentos.</p>
      </main>
      <Footer />
    </div>
  );
}

export default App;
import React from 'react';

function Footer() {
  return (
    <footer style={{
      backgroundColor: '#282c34', // Mismo color de fondo que el header para consistencia
      color: 'white',
      padding: '30px 20px',
      textAlign: 'center',
      marginTop: '60px', // Margen superior para separarlo del contenido
      borderTop: '1px solid #444', // Una línea superior para definirlo
      width: '100%', // Asegura que ocupe todo el ancho
      boxSizing: 'border-box', // Incluye padding y border en el ancho total
    }}>
      <div style={{ marginBottom: '15px' }}>
        <p>&copy; {new Date().getFullYear()} OcaWeb. Todos los derechos reservados.</p>
      </div>
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        gap: '20px', // Espacio entre los enlaces
      }}>
        <a href="/politica-cookies" style={{ color: 'white', textDecoration: 'none', transition: 'color 0.3s ease' }}>Política de Cookies</a>
        <a href="/politica-privacidad" style={{ color: 'white', textDecoration: 'none', transition: 'color 0.3s ease' }}>Política de Privacidad</a>
      </div>
    </footer>
  );
}

export default Footer;
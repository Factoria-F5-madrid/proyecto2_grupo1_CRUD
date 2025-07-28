// tailwind.config.js
// @type {import('tailwindcss').Config} 
module.exports = {
    content: [
      "./index.html", 
      "./src/**/*.{js,ts,jsx,tsx}", // ¡CRUCIAL! Esto busca en todos los archivos JS/TS/JSX/TSX dentro de 'src/'
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }
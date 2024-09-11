import React, { useRef, useState, useEffect } from 'react';
import { trainDecisionTree, trainRandomForest } from './services/apiService';

const DrawCanvas = () => {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);

  useEffect(() => {
    const canvas = canvasRef.current;
    console.log(canvas)
    const context = canvas.getContext('2d');

    // Configura el canvas: estilo del pincel
    context.lineWidth = 8; // Grosor del pincel
    context.lineCap = 'round'; // Pincel redondeado
    context.strokeStyle = 'black'; // Color del pincel

    // Fondo blanco para el canvas
    context.fillStyle = 'white';
    context.fillRect(0, 0, canvas.width, canvas.height);
  }, []);

  // Función para iniciar el dibujo
  const startDrawing = ({ nativeEvent }) => {
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext('2d');
    context.beginPath();
    context.moveTo(offsetX, offsetY);
    setIsDrawing(true);
  };

  // Función para continuar dibujando
  const draw = ({ nativeEvent }) => {
    if (!isDrawing) return;
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext('2d');
    context.lineTo(offsetX, offsetY);
    context.stroke();
  };

  // Función para finalizar el dibujo
  const endDrawing = () => {
    const context = canvasRef.current.getContext('2d');
    context.closePath();
    setIsDrawing(false);
  };

  // Función para limpiar el canvas
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    // Fondo blanco para el canvas
    context.fillStyle = 'white';
    context.fillRect(0, 0, canvas.width, canvas.height);
  };

  // Función para extraer la imagen dibujada (en formato Base64)
  const getImageData = () => {
    const canvas = canvasRef.current;
    const dataURL = canvas.toDataURL('image/png');
    console.log(dataURL); // Puedes enviar este dato a tu backend
    return dataURL;
  };

  const handleProcessDecissionTree = async () =>{
    var result = await trainDecisionTree(0.2, 42)
    var result = await trainRandomForest(0.2, 42, 100)
    getImageData()
    console.log(result)
  }

  return (
    <div>
      <canvas
        ref={canvasRef}
        width={300}
        height={300}
        style={{ border: '2px solid black', backgroundColor: 'white' }}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={endDrawing}
        onMouseLeave={endDrawing} // Finaliza el dibujo si el cursor sale del canvas
      />
      <div style={{ marginTop: '10px' }}>
        <button onClick={handleProcessDecissionTree}>Process Decission Tree</button>
        <button onClick={clearCanvas}>Clear Canvas</button>
        <button onClick={getImageData}>Get Image Data</button>
      </div>
    </div>
  );
};

export default DrawCanvas;

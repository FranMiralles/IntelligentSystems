import React, { useRef, useState, useEffect } from 'react'
import { trainDecisionTree, trainRandomForest, sendImage, trainAll } from './services/apiService'

const DrawCanvas = () => {
  const canvasRef = useRef(null)
  const [isDrawing, setIsDrawing] = useState(false)

  useEffect(() => {
    const canvas = canvasRef.current
    const context = canvas.getContext('2d')
    context.lineCap = 'round'
    context.strokeStyle = 'black'
    context.fillStyle = 'white'
    context.fillRect(0, 0, canvas.width, canvas.height)
  }, [])

  const startDrawing = ({ nativeEvent }) => {
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext('2d');
    context.lineCap = 'round';
    context.lineJoin = 'round';
    setIsDrawing(true);
    draw({ nativeEvent });
  };
  
  const draw = ({ nativeEvent }) => {
    if (!isDrawing) return;
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext('2d');
    
    // Crear degradado radial
    const gradient = context.createRadialGradient(offsetX, offsetY, 0, offsetX, offsetY, 15);
    gradient.addColorStop(0, 'rgba(0, 0, 0, 1)');
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
  
    // Aplicar el degradado como color del trazo
    context.strokeStyle = gradient;
    context.fillStyle = gradient;
    context.lineWidth = 20;
  
    context.beginPath();
    context.arc(offsetX, offsetY, 5, 0, Math.PI * 2);
    context.fill();
  
    context.stroke();
  };
  
  const endDrawing = () => {
    setIsDrawing(false);
  };
  
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = 'white';
    context.fillRect(0, 0, canvas.width, canvas.height);
  };
  

  const getImageData = () => {
    const canvas = canvasRef.current
    const dataURL = canvas.toDataURL('image/png')
    console.log(dataURL)
    return dataURL
  };

  const handleProcessDecissionTree = async () =>{
    var result = await trainDecisionTree(0.2, 42)
    var result = await trainRandomForest(0.2, 42, 100)
    getImageData()
    console.log(result)
  }

  const trainAllModels = () => {
    trainAll(0.15, 42, 100).then((res) => console.log(res))
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
        onMouseLeave={endDrawing}
      />
      <div style={{ marginTop: '10px' }}>
        <button onClick={()=>sendImage(getImageData())}>Send image</button>
        <button onClick={handleProcessDecissionTree}>Process Decission Tree</button>
        <button onClick={clearCanvas}>Clear Canvas</button>
        <button onClick={getImageData}>Get Image Data</button>
        <button onClick={trainAllModels}>TRAIN ALL</button>
      </div>
    </div>
  )
}

export default DrawCanvas

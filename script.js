async function descargar() {
  const url = document.getElementById("videoUrl").value;
  const mensaje = document.getElementById("mensaje");
  mensaje.textContent = "Descargando...";

  try {
    const response = await fetch("https://ytdwnldr.onrender.com/download", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    if (!response.ok) {
      throw new Error("Error al descargar el video");
    }

    const blob = await response.blob();
    const enlace = document.createElement("a");
    enlace.href = URL.createObjectURL(blob);
    enlace.download = "video.mp4";
    enlace.click();

    mensaje.textContent = "¡Descarga completada!";
  } catch (error) {
    console.error(error);
    mensaje.textContent = "Hubo un error al descargar el video.";
  }
}

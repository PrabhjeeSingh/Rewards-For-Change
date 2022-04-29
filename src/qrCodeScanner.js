const qrcode = window.qrcode;
const video = document.createElement("video");
const canvasElement = document.getElementById("qr-canvas");
const canvas = canvasElement.getContext("2d");
const qrResult = document.getElementById("qr-result");
const outputData = document.getElementById("outputData");
const btnScanQR = document.getElementById("btn-scan-qr");
let scanning = false;







qrcode.callback = (res) => {
    if (res) {
      outputData.innerText = res;
      scanning = false;
      video.srcObject.getTracks().forEach(track => {
        track.stop();
      });
      qrResult.hidden = false;
      btnScanQR.hidden = false;
      canvasElement.hidden = true;
    }
  };
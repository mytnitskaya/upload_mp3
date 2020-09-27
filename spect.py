import os
from flask import make_response
from pydub import AudioSegment
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.io import wavfile
from io import BytesIO

def spectogram(filepath): 
    mp3_audio = AudioSegment.from_file(filepath, format="mp3")  
    wname = "temp.wav" 
    mp3_audio.export(wname, format="wav")  
    FS, data = wavfile.read(wname)  
    data = data[:,0]

    fig = plt.figure()
    plt.specgram(data, Fs=FS, NFFT=128, noverlap=0) 
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    
    os.remove(wname)
    return response
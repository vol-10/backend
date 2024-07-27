from audiocraft.models import musicgen
from audiocraft.data.audio import audio_write
from pydub import AudioSegment
from flask import current_app

def create_bgm(emo_str, out_name, out_dur):
    '''
    引数
    emo_str:  感情の種類    ex: 'happy'
    out_name: 出力する音声ファイルの名前    ex: 'a'
    out_dur:  音声の長さ[秒]    ex: 6.0

    戻り値（仮）
    音声ファイルの名前
    '''
    #モデルの選択
    model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small')
    model.set_generation_params(
        duration = out_dur
    )
    #生成
    output = model.generate(
        descriptions = [
            emo_str
        ],
        progress = True
    )
    #保存
    sounds_path = current_app.config['UPLOAD_SOUNDS']
    audio_write(sounds_path + out_name,
                output[0].cpu(), model.sample_rate)
    notes = AudioSegment.from_wav(sounds_path + out_name + '.wav')
    notes.export(sounds_path + out_name + '.mp3', format="mp3")
    
    return out_name + '.mp3'

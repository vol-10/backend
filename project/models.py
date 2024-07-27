from audiocraft.models import musicgen
from audiocraft.data.audio import audio_write

sounds_path = './static/sounds/'

def create_bgm(emo_str, out_name, out_dur):
    '''
    引数
    emo_str:  感情の種類    ex: 'happy'
    out_name: 出力する音声ファイルの名前    ex: 'a'
    out_dur:  音声の長さ[秒]    ex: 6.0

    戻り値（仮）
    音声ファイルのパス
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
    audio_write(sounds_path + out_name,
                output[0].cpu(), model.sample_rate)
    
    return sounds_path + out_name

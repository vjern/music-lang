import { $ } from './select.js';
import Http from './http.js';

const onCtrlEnter = function(f, event) {
    if (
        (event.code === 'Enter' || event.code === 'NumpadEnter')
        && (event.ctrlKey)
    ) f();
}

const playAudio = () => {
    $('#dump audio').play();
}

const play = () => {
    let code = $('#textarea').value;
    let bpm = $('#bpm').value;
    Http.POST('/play', { code, bpm })
    .then(Http.assertParse)
    .then(rep => {
        $('#dump').innerHTML = `
        <audio controls>
            <source src="${rep.path}" type="audio/wav">
            Your browser does not support the audio tag.
        </audio> 
        `
    })
    .then(playAudio)
}

$('#textarea').addEventListener('keypress', onCtrlEnter.bind(null, play));
$('#play').addEventListener('click', play);

import { $ } from './select.js';
import Http from './http.js';

play = () => {
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
    .then(() => {
        $('#dump audio').play();
    })
}

$('#play').addEventListener('click', play);

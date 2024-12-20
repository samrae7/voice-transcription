## Loading and transforming AMI Dataset

•	Thirty-second audio chunks.
•	Labels for each one-second sub-interval within those chunks (e.g., 0 for no speaker change, 1 for a speaker change).
•	Optional: Metadata for each chunk, like the original file name and time range.

each item should be

- audio - mel spectogram of thorty seconds of audio
- labels - labels for each 1-sec chunk of the audio. Can just be 1 for speaker change, 0 for no change
- the text of the transcript ?

These are the first few samples of AMI

```
Example samples:
===============

Sample 0:
------------
meeting_id: EN2001a
audio_id: AMI_EN2001a_H04_MEO069_0330297_0330718
text: IF YOU IF YOU S. S. H. AND THEY HAVE THIS BIG WARNING ABOUT DOING NOTHING AT ALL IN THE GATEWAY MACHINE
audio: {'path': '/Users/samuelrae/.cache/huggingface/datasets/downloads/extracted/22a99373ac94f4569b64174a4d9b45013d6b8222d733c8941e305a942421455e/EN2001a/train_ami_en2001a_h04_meo069_0330297_0330718.wav', 'array': array([ 0.00231934, -0.00183105, -0.00543213, ..., -0.00238037,
       -0.00244141, -0.00219727]), 'sampling_rate': 16000}
begin_time: 3302.969970703125
end_time: 3307.179931640625
microphone_id: H04
speaker_id: MEO069

Sample 1:
------------
meeting_id: EN2001a
audio_id: AMI_EN2001a_H00_MEE068_0414915_0415078
text: I'VE GOTTEN MM HARDLY ANY
audio: {'path': '/Users/samuelrae/.cache/huggingface/datasets/downloads/extracted/22a99373ac94f4569b64174a4d9b45013d6b8222d733c8941e305a942421455e/EN2001a/train_ami_en2001a_h00_mee068_0414915_0415078.wav', 'array': array([-5.18798828e-04,  1.22070312e-04,  1.22070312e-04, ...,
        9.15527344e-05, -1.83105469e-04, -3.35693359e-04]), 'sampling_rate': 16000}
begin_time: 4149.14990234375
end_time: 4150.77978515625
microphone_id: H00
speaker_id: MEE068

Sample 2:
------------
meeting_id: EN2001a
audio_id: AMI_EN2001a_H03_MEE067_0319290_0319815
text: IT'S YEAH I MEAN THE WAVE DATA ARE OBVIOUSLY NOT GONNA GET OFF THERE COMPLETELY
audio: {'path': '/Users/samuelrae/.cache/huggingface/datasets/downloads/extracted/22a99373ac94f4569b64174a4d9b45013d6b8222d733c8941e305a942421455e/EN2001a/train_ami_en2001a_h03_mee067_0319290_0319815.wav', 'array': array([-0.00015259, -0.00021362, -0.00012207, ...,  0.00021362,
        0.00027466,  0.00033569]), 'sampling_rate': 16000}
begin_time: 3192.89990234375
end_time: 3198.14990234375
microphone_id: H03
speaker_id: MEE067

Sample 3:
------------
meeting_id: EN2001a
audio_id: AMI_EN2001a_H04_MEO069_0145515_0146152
text: YEAH IT'LL IT'LL PLAY THEM IN SOME ORDER IN WHICH THEY WERE SET BECAUSE OTHERWISE IT'S GONNA BE MORE ENTERTAINING
audio: {'path': '/Users/samuelrae/.cache/huggingface/datasets/downloads/extracted/22a99373ac94f4569b64174a4d9b45013d6b8222d733c8941e305a942421455e/EN2001a/train_ami_en2001a_h04_meo069_0145515_0146152.wav', 'array': array([ 0.00000000e+00,  0.00000000e+00,  6.10351562e-05, ...,
       -6.10351562e-05, -6.10351562e-05, -3.05175781e-05]), 'sampling_rate': 16000}
begin_time: 1455.1500244140625
end_time: 1461.52001953125
microphone_id: H04
speaker_id: MEO069

Sample 4:
------------
meeting_id: EN2001a
audio_id: AMI_EN2001a_H03_MEE067_0478127_0478164
text: YEAH
audio: {'path': '/Users/samuelrae/.cache/huggingface/datasets/downloads/extracted/22a99373ac94f4569b64174a4d9b45013d6b8222d733c8941e305a942421455e/EN2001a/train_ami_en2001a_h03_mee067_0478127_0478164.wav', 'array': array([-0.00149536, -0.00149536, -0.00158691, ..., -0.00027466,
       -0.00021362, -0.00018311]), 'sampling_rate': 16000}
begin_time: 4781.27001953125
end_time: 4781.64013671875
microphone_id: H03
speaker_id: MEE067
```

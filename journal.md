## Dataset

•	Thirty-second audio chunks.
•	Labels for each one-second sub-interval within those chunks (e.g., 0 for no speaker change, 1 for a speaker change).
•	Optional: Metadata for each chunk, like the original file name and time range.

each item should be

- audio - mel spectogram of thorty seconds of audio
- labels - labels for each 1-sec chunk of the audio. Can just be 1 for speaker change, 0 for no change
- the text of the transcript ?


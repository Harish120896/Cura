:loop
python -m scripts.label_image  --graph=tf_files/retrained_graph.pb    --image=local-filename.jpg
goto loop
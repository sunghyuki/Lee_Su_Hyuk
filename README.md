"# Lee_Su_Hyuk" 

데이터 셋 : 버스 정류장에서 직접 촬영

labelimg를 이용하여 xml 파일로 라벨링

이미지와 xml 파일을 9:1 비율로
train, test 폴더로 복사
xml_to_csv.py을 이용해 xml파일들을 csv로 변환해서 data 폴더에 저장

아래 두 명령어를 이용해서 train.record와 test.record를 생성
python generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record --image_dir=images/train

python generate_tfrecord.py --csv_input=data/test_labels.csv --output_path=data/test.record --image_dir=images/test


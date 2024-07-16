// import React from 'react'
import {useState, useEffect, useRef} from "react"
import Card from "./Card";

export default function Prac1() {
    // 변수, 함수, useEffect 선언

    const [tdata, setTdata] = useState([]);
    const [tags, setTags] = useState([]);
    const getData = (keyword)=>{
        // API 가져올 URL 변수는 let으로 선언
        let url = 'https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?';
        url = url + `serviceKey=${process.env.REACT_APP_API_KEY}`;
        url = url + '&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A';
        url = url + `&keyword=${keyword}&_type=json`;
        console.log(url);
    
        //setTdata 함수 : tdata[]에 URL에서 가져온 정보를 저장
        fetch(url)
        .then(resp => resp.json())
        .then(data => setTdata(data.response.body.items.item))
        ;
    }

    // 확인 버튼 -> 누르면 input 박스의 내용이 inRef를 통해 전달
    const inRef = useRef();
    const handleClick = (e)=>{
        e.preventDefault();

        let keyword = encodeURI(inRef.current.value);
        getData(keyword);
    }

    //tData 변경되었을 때
    useEffect(()=>{
      let tm = tdata.map(item => <Card key={item.galContentId}
                                       galTitle = {item.galTitle}
                                       galWebImageUrl = {item.galWebImageUrl}/>);
      setTags(tm);
  }, [tdata]);

  return (
    <div className="flex flex-col">
      <form className='w-full flex m-5'>
        <input type='text' id='inputBox'
               ref={inRef}
               className='placeholder="키워드 입력" text-gray-500'></input>
      
        <button className='bg-gray-600 text-white text-lg p-5'
                onClick={handleClick}>확인</button>
      </form>
      <div className='h-full text-gray-600
                            grid grid-cols-1 gap-4
                            md:grid-cols-3'>
        {tags}
      </div>
    </div>
  )
}

// import React from 'react'
import {useState, useEffect, useRef} from "react"

export default function Prac1() {
    // 변수, 함수, useEffect 선언

    const [tdata, setTdata] = useState([]);
    const getData = (keyword)=>{
        // API 가져올 URL 변수는 let으로 선언
        let url = 'https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?';
        url = url + `serviceKey=${process.env.REACT_APP_API_KEY}`;
        url = url + '&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A';
        url = url + `&keyword=${keyword}&_type=json`;
    
        fetch(url)
        .then(resp => resp.json())
        .then(data => setTdata(data.response.body.items.item))
        ;
    }

    // 확인 버튼 -> 누르면 input 박스의 내용이 inRef를 통해 전달
    const inRef = useRef();
    const handleClick = (e)=>{
        e.preventDefault();
        let kw = encodeURI(inRef.current.value);
        getData(kw);
    }

  return (
    <div>
      
    </div>
  )
}

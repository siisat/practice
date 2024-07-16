// import React from 'react'

export default function Card({galTitle, galWebImageUrl}) {
  return (
    <div className="text-sm bg-white border border-gray-200 rounded-lg shadow">
      <img className="rounded-t-lg"
           src={galWebImageUrl} alt=""></img>
      <div>
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900">
            {galTitle}</h5>
      </div>
    </div>
  )
}

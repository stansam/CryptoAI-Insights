import React, { useEffect } from 'react'
import videos from "./../MOCK_DATA/MOCK_VIDEOS"

const MainContent = () => {

    useEffect(() => console.log(videos))
    return (
        <div>
            <div>
                <span>Tranding</span>
                <div>{videos.map(video => <li>{video.title}</li>)}</div>
            </div>
            <div>
                <span>Tokens</span>
                <div></div>
            </div>
        </div>
    )
}

export default MainContent

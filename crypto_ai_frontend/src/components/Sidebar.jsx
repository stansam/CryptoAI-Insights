import React from 'react'

const Sidebar = () => {
    return (
        <section>
            <div>
                <h2>Look up Recommendations</h2>
                <ul>
                    <li>
                        <a href="https://localhost:3000/">By Influencer</a>
                        <a href="https://localhost:3000/">By Token</a>
                        <a href="https://localhost:3000/">By Social Media Platform</a>
                        <div>
                            <a href="https://localhost:3000/">By Category</a>
                            <ul>
                                <li>
                                    <a href="https://localhost:3000/">Stable Coins</a>
                                </li>
                                <li>
                                    <a href="https://localhost:3000/">Alt Coins</a>
                                </li>
                                <li>
                                    <a href="https://localhost:3000/">Meme Coins</a>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ul>
            </div>
        </section>
    )
}

export default Sidebar

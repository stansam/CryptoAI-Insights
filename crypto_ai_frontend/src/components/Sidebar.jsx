import React from 'react'

const Sidebar = () => {
    return (
        <section className='w-1/4 p-3 h-screen bg-yellow-200 pt-10'>
            <div>
                <h2 className='font-bold my-5 text-xl'>Look up Recommendations</h2>
                <ul className='font-semibold'>
                    <li className='hover:-translate-y-1 hover:transition-transform m-4'>
                        <a href="https://localhost:3000/">By Influencer</a>
                    </li>
                    <li className='hover:-translate-y-1 hover:transition-transform m-4'>
                        <a href="https://localhost:3000/">By Token</a>
                    </li>
                    <li className='hover:-translate-y-1 hover:transition-transform m-4'>
                        <a href="https://localhost:3000/">By Social Media Platform</a>
                    </li>
                    <li className='m-4'>
                        <a href="https://localhost:3000/">By Category</a>
                        <ul>
                            <li className='hover:-translate-y-1 hover:transition-transform m-4 font-normal text-gray-600'>
                                <a href="https://localhost:3000/">Stable Coins</a>
                            </li>
                            <li className='hover:-translate-y-1 hover:transition-transform m-4 font-normal text-gray-600'>
                                <a href="https://localhost:3000/">Alt Coins</a>
                            </li>
                            <li className='hover:-translate-y-1 hover:transition-transform m-4 font-normal text-gray-600'>
                                <a href="https://localhost:3000/">Meme Coins</a>
                            </li>
                        </ul>
                    </li>
                    <li className='hover:-translate-y-1 hover:transition-transform m-4'>
                        <a href="https://localhost:3000/">Porfolios of Influencers</a>
                    </li>
                    <li className='hover:-translate-y-1 hover:transition-transform m-4'>
                        <a href="https://localhost:3000/">Portfolio Competition (Beat the Experts)</a>
                    </li>
                </ul>
            </div>
        </section>
    )
}

export default Sidebar

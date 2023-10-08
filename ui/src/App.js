import {useEffect, useState} from 'react';
import './App.scss'
import Navbar from "./components/Navbar/navbar";
import Button from "./components/Button/button";
import Items from "./pages/Items";
import Home from "./pages/Home";
import Games from "./pages/Games";
import { Route, Routes } from "react-router-dom";

export default function App() {

    return (
        <>
            <Navbar />
            <div className="container">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/games" element={<Games />} />
                    <Route path="/items" element={<Items />} />
                </Routes>
            </div>
        </>
    );
}
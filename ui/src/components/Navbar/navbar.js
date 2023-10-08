import Button from "../Button/button";
import { Link, useMatch, useResolvedPath } from "react-router-dom";

const Navbar = () => {

    return (
        <nav className="nav">
            <Link to="/" className="site-title">
                Steam Market
            </Link>
            <ul>
                <CustomLink to="/">Home</CustomLink>
                <CustomLink to="/games">Games</CustomLink>
                <CustomLink to="/items">Items</CustomLink>
            </ul>
        </nav>

    )
}

function CustomLink({ to, children, ...props }) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname, end: true })
    return (
        <li className={isActive ? "active" : ""}>
            <Link to={to} {...props}>
                {children}
            </Link>
        </li>
    )
}

export default Navbar

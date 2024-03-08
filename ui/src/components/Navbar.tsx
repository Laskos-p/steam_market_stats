import { Link, NavLink, NavLinkProps } from "react-router-dom";
import clsx from "clsx/lite";

const Navbar = () => {
  return (
    <div className="flex items-center justify-between bg-primary p-4 ring-[1rem] ring-secondary">
      <Link to="/">
        <h1>Steam Market</h1>
      </Link>
      <nav>
        <ul className="flex h-full gap-4">
          <li>
            <CustomLink to="/">Home</CustomLink>
          </li>
          <li>
            <CustomLink to="/items">Items</CustomLink>
          </li>
        </ul>
      </nav>
    </div>
  );
};

function CustomLink({ to, children, ...props }: NavLinkProps) {
  return (
    <NavLink
      to={to}
      {...props}
      className={({ isActive }) =>
        clsx(
          "grid aspect-video items-center px-4 hover:bg-[#777] focus-visible:bg-[#777]",
          isActive && "bg-[#555]",
        )
      }
    >
      {children}
    </NavLink>
  );
}

export default Navbar;

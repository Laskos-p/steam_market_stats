import { Link, LinkProps, useMatch, useResolvedPath } from "react-router-dom";
import clsx from "clsx/lite";

const Navbar = () => {
  return (
    <nav className="sticky top-0 flex justify-between bg-[#333] px-4 text-white">
      <Link to="/">
        <h1>Steam Market</h1>
      </Link>
      <ul className="flex gap-4">
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/games">Games</CustomLink>
        <CustomLink to="/items">Items</CustomLink>
      </ul>
    </nav>
  );
};

function CustomLink({ to, children, ...props }: LinkProps) {
  const resolvedPath = useResolvedPath(to);
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });
  return (
    <li className={clsx("hover:bg-[#777]", isActive && "bg-[#555]")}>
      <Link
        to={to}
        {...props}
        className={clsx("grid h-full place-items-center", props.className)}
      >
        {children}
      </Link>
    </li>
  );
}

export default Navbar;

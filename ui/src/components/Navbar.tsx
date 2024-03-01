import { Link, LinkProps, useMatch, useResolvedPath } from "react-router-dom";
import clsx from "clsx/lite";

const Navbar = () => {
  return (
    <header className="sticky top-0 flex justify-between bg-primary px-4 py-2 ring-[1rem] ring-secondary">
      <h1>
        <Link to="/">Steam Market</Link>
      </h1>
      <nav>
        <ul className="flex h-full gap-4">
          <CustomLink to="/">Home</CustomLink>
          <CustomLink to="/items">Items</CustomLink>
        </ul>
      </nav>
    </header>
  );
};

function CustomLink({ to, children, ...props }: LinkProps) {
  const resolvedPath = useResolvedPath(to);
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });
  return (
    <li
      className={clsx(
        "px-2 focus-within:bg-[#777] hover:bg-[#777]",
        isActive && "bg-[#555]",
      )}
    >
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

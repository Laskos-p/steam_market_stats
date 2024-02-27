import React from "react";
import { Link, LinkProps, useMatch, useResolvedPath } from "react-router-dom";
import clsx from "clsx/lite";

const Navbar = () => {
  return (
    <nav className="flex justify-between bg-[#333] px-4 text-white">
      <Link to="/" className="text-[2rem]">
        Steam Market
      </Link>
      <ul className="flex gap-4">
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/games">Games</CustomLink>
        <CustomLink to="/items">Items</CustomLink>
      </ul>
    </nav>
  );
};

interface CustomLinkProps extends LinkProps {
  to: string;
  children: React.ReactNode;
}

function CustomLink({ to, children, ...props }: CustomLinkProps) {
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
